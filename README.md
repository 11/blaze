# Blaze 🔥

### Description
Blaze is a site generator CLI for single-page applications developed with [lit-element](https://lit.dev) - as well as build tool for traditional static websites. Blaze comes bundled with its own flavor of Mdx that integrates native web-components and lit-element syntax directly into a Markdown file. Blaze's goal is to abstract away the tedious build steps, enable you to quickly iterate on static content, and bind the result into a lean front-end app.

---

### How to use:
Blaze comes bundled with 3 simple commands: `init`, `build`, `serve`.

### Init
The `init` command will set a directory as a blaze project and configure the project folder structure. Depending on the type of project (`static` or `single-page`), the project structure will be differently as well as install Javascript dependencies. 
- `static` is similar to a jekyll project 
- `single-page` is similar to a create-react-app project

```bash
# Bash command arguments 
$ blaze init --type={ static, single-page } [directory]

# Examples:
# make current directory a `static` blaze application - blaze defaults `--type=static`
$ blaze init

# make the `Desktop/personal-site/` directory a lit-element single-page app
$ blaze init --type=single-page Desktop/personal-site/
``` 

#### Build

The `build` command will simply compile all the `.mdx` files in your project. If you are working on a `static` website, this step will output `.html` files. If you are working on `single-page` app, this step will output a JSON file that will be asynchronously imported as a route. 

The `build` command doesn't take in any parameters, but must be run from within your blaze project. Blaze will know if it's inside your project by recrusvely checking for a `blaze.json` file. The `blaze.json` is considered to be the root of your Blaze project.

```bash
user@~/Code/blaze-project $ blaze build
```

#### Serve
The `serve` command will take the built version of your project and run it locally. If you are working on a `static` project, this step will run a dev HTTP web server. If you are working on a `single-page` app, this will run a `webpack-dev-server` and listen for when local files change.

Similar to the `build command, the `serve` command must be run somewhere within your project. 

```bash
user@~/Code/blaze-project $ blaze serve
```

---

### Customization

You can modify many of your Blaze project's settings to your liking. These are the current settings you can update inside your `blaze.json`

| Variable | Description |
| -------- | ----------- |
| `entries`  | The directory that stores your `.mdx` files |
| `views`    | The directory `blaze build` will output your compiled markdown |
| `port`     | The port your dev server will run on |
| `project`  | The project type either `static` or `single-page` |
