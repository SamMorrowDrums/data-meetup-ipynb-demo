#!/bin/bash
if [ -x $0.local ]; then
    $0.local "$@" || exit $?
fi
if [ -x tracked-hooks/$(basename $0) ]; then
    tracked-hooks/$(basename $0) "$@" || exit $?
fi
