cd ~/studio/targets/kettle-desktop
cp ../kettle-web/brew.js ../kettle-web/index.html .
npm init -y
npm install --save-dev electron
npx electron .
npx @electron/asar pack . ../kettle-desktop.asar
