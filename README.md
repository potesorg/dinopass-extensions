# Dinopass Extension

Chrome extension used to generate strong passwords in the browser.

## Features:

* easy to load into Chrome based broswers
* Simple popup GUI
* copy button functionality for easse of use


## How does it work?

### Adding
The chrome extension can be loaded into your browser using the `Extensions` function is Chrome.

For more info on custom extensions, see [this](https://support.google.com/chrome_webstore/answer/2664769?hl=en) article.

### Under the hood

The extension is a simple plugin that has no functional logic.

Once loaded, clicking on the extension will open up a popup with a button to generate a new password. Once clicked, the extension executes a call to the [Dinopass API](https://www.dinopass.com/api). At the current stage, all passwords will be generated using the `/strong` endpoint.

For more information, refer to the documentation of the Dinopass API. 

When the Api call has finished and a response is received, the new password will be displayed in the popup. A `Copy` button becomes available, which will use the native browser clipboard functionality to copy the newly generated password to your clipboard.

## How to improve locally

The repo contains all the files needed to compile the extension.

The `src/index.js` file contains the required API call and the copying logic. 

In the `package.json` file, use the `build` script to compile the extension. 

#### Further improvements:

* better UI
* option to generate simple/strong passwords
* input field for username (async, no data is stored)
* export to JSON for storing