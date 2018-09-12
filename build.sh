#bin/bash

rm -rf server/build
cd hostel-app-react && npm run build && cd ..
mv hostel-app-react/build server/build

set -e