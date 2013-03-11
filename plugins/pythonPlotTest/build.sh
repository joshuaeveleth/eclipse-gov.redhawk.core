#!/bin/sh

if [ "$1" == "rpm" ]; then
    # A very simplistic RPM build scenario
    if [ -e pythonPlotTest.spec ]; then
        mydir=`dirname $0`
        tmpdir=`mktemp -d`
        cp -r ${mydir} ${tmpdir}/pythonPlotTest-1.0.0
        tar czf ${tmpdir}/pythonPlotTest-1.0.0.tar.gz --exclude=".svn" -C ${tmpdir} pythonPlotTest-1.0.0
        rpmbuild -ta ${tmpdir}/pythonPlotTest-1.0.0.tar.gz
        rm -rf $tmpdir
    else
        echo "Missing RPM spec file in" `pwd`
        exit 1
    fi
else
    for impl in python ; do
        pushd $impl &> /dev/null
        if [ -e build.sh ]; then
            ./build.sh $*
        else
            echo "No build.sh found for $impl"
        fi
        popd &> /dev/null
    done
fi
