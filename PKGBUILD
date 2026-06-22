pkgname=terminator-package-manager
pkgver=0.1
pkgrel=1
pkgdesc="Terminator Game Package Manager"
arch=('x86_64')
depends=('python' 'wget')
license=('GPL3')

source=()

package() {
    mkdir -p "$pkgdir/terminator/files"

    cp ../cli.py "$pkgdir/terminator/files/"
    cp -r ../core "$pkgdir/terminator/files/"

    find "$pkgdir/terminator/files" -type d -exec chmod 755 {} \;
    find "$pkgdir/terminator/files" -type f -exec chmod 755 {} \;

    mkdir -p "$pkgdir/usr/bin"

    ln -s /terminator/files/cli.py \
        "$pkgdir/usr/bin/terminator-pm"
}
