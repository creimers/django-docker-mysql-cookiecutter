#!/usr/bin/env sh
#find . -name "*.jade" -exec sed -i '' -e 's/\.jade/\.html/' {} ";" &&
find . -name "*.jade" | sed 'p;s/\.jade/\.html/' | xargs -n2 pyjade
