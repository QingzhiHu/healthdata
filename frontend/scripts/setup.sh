#!/bin/bash
REACT_DASH_REPO="https://github.com/NuCivic/react-dash.git"
TIMESTAMP=$( date +%s )
DASH_LIB_NAME='react-dash'
SED="sed"
if [ "$(uname)" == "Darwin" ]; then
  SED="./bin/gsed"
fi

# make a backup directory
if [ ! -d backups ]; then
   echo "Creating backup directory"
    mkdir backups
fi

# if src directory exists, create backup first
if [ -d "src" ]; then
    BU_SRCDIR="backups/_src_$TIMESTAMP"
    echo "Backing up current /src dir to $BU_SRCDIR"
    mv src $BU_SRCDIR
fi

# build /src directory from react dash repo
echo "Copying boilerplate project from react-dashboard/examples"
mkdir src
cp -r node_modules/$DASH_LIB_NAME/examples/* src

# update import statements
find src -type f -exec perl -p -i -e "s/\.\.\/\.\.\/src(.*)/$DASH_LIB_NAME'/g" {} \;
find src -type f -exec perl -p -i -e "s/\.\.\/src(.*)/$DASH_LIB_NAME'/g" {} \;
#find src -type f -exec perl -p -i -e "s/import(.*)from 'react-dash'/import {\1} from '$DASH_LIB_NAME'/g" {} \;
#find src -type f -exec sed -i -E "s/import(.*)from '$DASH_LIB_NAME'/import {\1} from '$DASH_LIB_NAME'/g" {} \;
# rewrite "{ { library } }" as "{ library }"
find src -type f -exec $SED -i -E "s/\{ \{(.*)\} \}/\1/g" {} \;

# move resources to src folder
find src -type f -exec grep "$DASH_LIB_NAME" {} \;
echo "move example data to web-servable director /data"
cp -r node_modules/$DASH_LIB_NAME/examples/data/ data/

