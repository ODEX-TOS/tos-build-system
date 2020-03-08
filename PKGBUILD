# Maintainer: Tom Meyers tom@odex.be
pkgname=tos-build-system
pkgver=r1
pkgrel=1
pkgdesc="Build system to easily integrate tos functionality on your system"
arch=(any)
url="https://github.com/ODEX-TOS/tos-installer-backend"
_reponame="tos-build-system"
license=('MIT')

source=(
"git+https://github.com/ODEX-TOS/tos-build-system.git")
md5sums=('SKIP')
depends=('python')
makedepends=('git')

pkgver() {
  cd "$srcdir/$_reponame"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}


build() {
    return 0;
}

package() {
        cd "$srcdir/$_reponame"
        python setup.py  install --root="${pkgdir}"
        install -Dm755 tbs "$pkgdir"/usr/bin/tbs
}