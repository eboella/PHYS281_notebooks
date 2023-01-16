MODULE types
  ! Double and quadruple precision kinds.  Seems to be necessary to place these
  ! in a separate module.
  IMPLICIT NONE
  INTEGER,PARAMETER :: sp=KIND(1.0)
  INTEGER,PARAMETER :: dp=KIND(1.d0)
  INTEGER,PARAMETER :: qp=selected_real_KIND(2*PRECISION(1.d0))
END MODULE types


MODULE utils
  ! Fortran utilities to calculate the Mandelbrot set.
  USE types,ONLY : sp,dp,qp
  IMPLICIT NONE
  INTEGER,PARAMETER :: colourscale=1
  INTEGER,PARAMETER :: colourrange=255 ! Number of non-black colours?


CONTAINS


  PURE INTEGER FUNCTION mandel_dp(cx,cy,smax)
    ! Determine whether cx+i.cy is in the Mandelbrot set.  Return zero if yes;
    ! otherwise returns a number proportional to the number of iterations
    ! required to reach |z|>2.  Double-precision version.
    IMPLICIT NONE
    INTEGER,INTENT(in) :: smax
    REAL(dp),INTENT(in) :: cx,cy
    INTEGER :: i
    COMPLEX(dp) :: c,z
    c=CMPLX(cx,cy,dp)
    z=c
    DO i=1,smax
      z=z*z+c
      IF(REAL(z,dp)**2+AIMAG(z)**2>=4.0_dp)THEN
        mandel_dp=colourrange-MOD(i*colourscale,colourrange)
        RETURN
      ENDIF ! |z|>=2
    ENDDO ! i
    mandel_dp=0
  END FUNCTION mandel_dp


  PURE INTEGER FUNCTION mandel_sp(cx,cy,smax)
    ! Single-precision version of mandel_dp.
    IMPLICIT NONE
    INTEGER,INTENT(in) :: smax
    REAL(sp),INTENT(in) :: cx,cy
    INTEGER :: i
    COMPLEX(sp) :: c,z
    c=CMPLX(cx,cy,sp)
    z=c
    DO i=1,smax
      z=z*z+c
      IF(REAL(z,sp)**2+AIMAG(z)**2>=4.0_sp)THEN
        mandel_sp=colourrange-MOD(i*colourscale,colourrange)
        RETURN
      ENDIF ! |z|>=2
    ENDDO ! i
    mandel_sp=0
  END FUNCTION mandel_sp


  PURE INTEGER FUNCTION mandel_qp(cx,cy,smax)
    ! Quadruple-precision version of mandel_dp.
    IMPLICIT NONE
    INTEGER,INTENT(in) :: smax
    REAL(qp),INTENT(in) :: cx,cy
    INTEGER :: i
    COMPLEX(qp) :: c,z
    c=CMPLX(cx,cy,qp)
    z=c
    DO i=1,smax
      z=z*z+c
      IF(REAL(z,qp)**2+AIMAG(z)**2>=4.0_qp)THEN
        mandel_qp=colourrange-MOD(i*colourscale,colourrange)
        RETURN
      ENDIF ! |z|>=2
    ENDDO ! i
    mandel_qp=0
  END FUNCTION mandel_qp


  SUBROUTINE mandelstring_dp(nx,ny,cxmin,cxmax,cymin,cymax,pixels)
    ! Return a string to create a bitmap of the Mandelbrot set in Tk.
    ! Double-precision version.
    IMPLICIT NONE
    INTEGER,INTENT(in) :: nx,ny
    REAL(dp),INTENT(in) :: cxmin,cxmax,cymin,cymax
    CHARACTER(ny*(4+nx*8)),INTENT(out) :: pixels
    INTEGER :: i,ix,iy,rowsize,nxm1,nym1,smax
    REAL(dp) :: dx,dy,cx,cy

    smax=MIN(NINT(MAX(-400.0_dp*LOG(cxmax-cxmin),100.0_dp)),100000)

    rowsize=4+nx*8 ; nxm1=nx-1 ; nym1=ny-1
    dx=(cxmax-cxmin)/REAL(nxm1,dp)
    dy=(cymax-cymin)/REAL(nym1,dp)
    !$OMP PARALLEL DO DEFAULT(none) SHARED(nx,ny,pixels,rowsize,nxm1,nym1,dx,&
    !$OMP   &dy,cxmin,cymin,smax) PRIVATE(ix,iy,i,cx,cy) SCHEDULE(STATIC,1)
    DO iy=0,ny-1
      cy=cymin+iy*dy
      cx=cxmin
      i=(nym1-iy)*rowsize+1
      pixels(i:i+1)='{ '
      i=i+2
      DO ix=0,nxm1
        WRITE(pixels(i:i+7),'("#",z2.2,"0000 ")')mandel_dp(cx,cy,smax)
        i=i+8
        cx=cx+dx
      ENDDO ! ix
      pixels(i:i+1)='} '
    ENDDO ! iy
    !$OMP END PARALLEL DO

  END SUBROUTINE mandelstring_dp


  SUBROUTINE mandelstring_sp(nx,ny,cxmin,cxmax,cymin,cymax,pixels)
    ! Single-precision version of mandelstring_dp.
    IMPLICIT NONE
    INTEGER,INTENT(in) :: nx,ny
    REAL(sp),INTENT(in) :: cxmin,cxmax,cymin,cymax
    CHARACTER(ny*(4+nx*8)),INTENT(out) :: pixels
    INTEGER :: i,ix,iy,rowsize,nxm1,nym1,smax
    REAL(sp) :: dx,dy,cx,cy

    smax=MIN(NINT(MAX(-400.0_sp*LOG(cxmax-cxmin),100.0_sp)),100000)

    rowsize=4+nx*8 ; nxm1=nx-1 ; nym1=ny-1
    dx=(cxmax-cxmin)/REAL(nxm1,sp)
    dy=(cymax-cymin)/REAL(nym1,sp)
    !$OMP PARALLEL DO DEFAULT(none) SHARED(nx,ny,pixels,rowsize,nxm1,nym1,dx,&
    !$OMP   &dy,cxmin,cymin,smax) PRIVATE(ix,iy,i,cx,cy) SCHEDULE(STATIC,1)
    DO iy=0,ny-1
      cy=cymin+iy*dy
      cx=cxmin
      i=(nym1-iy)*rowsize+1
      pixels(i:i+1)='{ '
      i=i+2
      DO ix=0,nxm1
        WRITE(pixels(i:i+7),'("#",z2.2,"0000 ")')mandel_sp(cx,cy,smax)
        i=i+8
        cx=cx+dx
      ENDDO ! ix
      pixels(i:i+1)='} '
    ENDDO ! iy
    !$OMP END PARALLEL DO

  END SUBROUTINE mandelstring_sp


  SUBROUTINE mandelstring_qp(nx,ny,cxmin,cxmax,cymin,cymax,pixels)
    ! Quadruple-precision version of mandelstring_dp.
    IMPLICIT NONE
    INTEGER,INTENT(in) :: nx,ny
    REAL(qp),INTENT(in) :: cxmin,cxmax,cymin,cymax
    CHARACTER(ny*(4+nx*8)),INTENT(out) :: pixels
    INTEGER :: i,ix,iy,rowsize,nxm1,nym1,smax
    REAL(qp) :: dx,dy,cx,cy

    smax=MIN(NINT(MAX(-400.0_qp*LOG(cxmax-cxmin),100.0_qp)),100000)

    rowsize=4+nx*8 ; nxm1=nx-1 ; nym1=ny-1
    dx=(cxmax-cxmin)/REAL(nxm1,qp)
    dy=(cymax-cymin)/REAL(nym1,qp)
    !$OMP PARALLEL DO DEFAULT(none) SHARED(nx,ny,pixels,rowsize,nxm1,nym1,dx,&
    !$OMP   &dy,cxmin,cymin,smax) PRIVATE(ix,iy,i,cx,cy) SCHEDULE(STATIC,1)
    DO iy=0,ny-1
      cy=cymin+iy*dy
      cx=cxmin
      i=(nym1-iy)*rowsize+1
      pixels(i:i+1)='{ '
      i=i+2
      DO ix=0,nxm1
        WRITE(pixels(i:i+7),'("#",z2.2,"0000 ")')mandel_qp(cx,cy,smax)
        i=i+8
        cx=cx+dx
      ENDDO ! ix
      pixels(i:i+1)='} '
    ENDDO ! iy
    !$OMP END PARALLEL DO

  END SUBROUTINE mandelstring_qp


END MODULE utils


SUBROUTINE gen_mandelstring(nx,ny,cxmin,cxmax,cymin,cymax,pixels)
  ! Return a string to create a bitmap of the Mandelbrot set in Tk.
  ! Select double- or quadruple-precision version.
  USE types,ONLY : dp,sp,qp
  USE utils,ONLY : mandelstring_dp,mandelstring_sp,mandelstring_qp
  IMPLICIT NONE
  INTEGER,INTENT(in) :: nx,ny
  REAL(dp),INTENT(in) :: cxmin,cxmax,cymin,cymax
  CHARACTER(ny*(4+nx*8)),INTENT(out) :: pixels
  REAL(dp),PARAMETER :: tol_sp=1.d-7,tol_dp=1.d-14,tol_qp=1.d-28
  REAL(dp) spacing
  spacing=MIN((cxmax-cxmin)/REAL(nx,dp),(cymax-cymin)/REAL(ny,dp))
  IF(spacing>tol_sp)THEN
    CALL mandelstring_sp(nx,ny,REAL(cxmin,sp),REAL(cxmax,sp),REAL(cymin,sp),&
      &REAL(cymax,sp),pixels)
  ELSEIF(spacing>tol_dp)THEN
    CALL mandelstring_dp(nx,ny,cxmin,cxmax,cymin,cymax,pixels)
  ELSEIF(spacing>tol_qp)THEN
    CALL mandelstring_qp(nx,ny,REAL(cxmin,qp),REAL(cxmax,qp),REAL(cymin,qp),&
      &REAL(cymax,qp),pixels)
  ELSE ! Hopeless.
    pixels=''
  ENDIF ! Double or quadruple prec?
END SUBROUTINE gen_mandelstring
