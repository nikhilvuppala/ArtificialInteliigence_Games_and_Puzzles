# TypeScript Joueur Client

**NOTE**: This is basically an advanced version of our [JavaScript client]. Consider this if you want bleeding edge Node with modern JS development using [TypeScript] and modern ES6 features. If you are not comfortable with TS know that all valid JS is valid TS too so you do not _need_ to know TS to use this client.

This is the client for the [Cadre] AI framework. It can play multiple different games, though you will probably only be interested in one at a time.

In general, try to stay out of the `src/joueur/` folder, it does most of the heavy lifting to play on our game servers.

Each AI, and the game objects it manipulates are all in `src/games/game-name/`, with your very own AI living in `src/games/game-name/ai.ts` for you to make smarter.

## How to Run

This client has been tested and confirmed to work on the MST campus rc##xcs213 Linux machines, but it can work on your own Windows/Linux/Mac machines if you desire.

### Requirements

The only requirement is [Node.js] version >= 10, which should include `node` and `npm`. Older versions _may_ or as
well, however we make no guarantees.

A `.nvmrc` file included is our recommended version, and we try to keep it up to date for you.

### Building

If you are using your own Linux/Mac make sure you have [Node.js] installed, then:

For all operating systems, you should only need to do the following:

```bash
npm install
npm run build
```

For any subsequent builds of the TypeScript compiler you just need to run `npm run build` again.

### Running

By default, the JS built is output to the `dist/` directory. You can then run them via:

```bash
npm start
```

or

```bash
node dist/
```

### Vagrant

Install [Vagrant] and [Virtualbox] in order to use the Vagrant configuration we provide which satisfies all build dependencies inside of a virtual machine. This will allow for development with your favorite IDE or editor on your host machine while being able to run the client inside the virtual machine. Vagrant will automatically sync the changes you make into the virtual machine that it creates. In order to use vagrant **after installing the aforementioned requirements** simply run from the root of this client:

```bash
vagrant up
```

and after the build has completed you can ssh into the virtual environment by running:

```bash
vagrant ssh
```

From there you will be in a Linux environment that has all the dependencies you'll need to build and run this client.

When the competition is over, or the virtual environment becomes corrupted in some way, simply execute `vagrant destroy` to delete the virtual machine and its contents.

For a more in depth guide on using vagrant, take a look at [Vagrant's guide].

#### Windows

Using Vagrant with Windows can be a bit of a pain. Here are some tips:

* Use an OpenSSH compatible ssh client. We recommend [Git Bash] to serve double duty as your git client and ssh client
* Launch the terminal of your choice (like Git Bash) as an Administrator to ensure the symbolic links can be created when spinning up your Vagrant virtual machine

## ES6 Coding

**You must know how to use [async/await] syntax**.

Whenever you invoke a function on a game object, it must ask our game server for the result. This is an asynchronous operation that returns a `Promise` with the return value.

For example, in chess you should do the following to move a piece:

```js
const move = await piece.move("a", 1);
```

## TSlint

By default we also include [TSLint] with your project. It just uses the Microsoft recommended rules, though you are free to change them to your preferences. We suggest ignoring our files as our style may not meet yours. The default `tslint.json` file does this for you.

## Dependencies

By default we include some dependencies in your `package.json`, such as `typescript` and `tslint`. You are free to add your own. However please don't remove the included packages, as they are required to run the base client.

## Other Notes

If you wish to use a different version of node, edit your `.nvmrc`, which will tell [Node Version Manager] your desired node version.

We **strongly** recommend using [Visual Studio Code] to develop and debug your code using this client.

It is possible that on your Missouri S&T S-Drive this client will not run properly. This is not a fault with the client, but rather the school's S-Drive implementation changing some file permissions during run time. We cannot control this. Instead, we recommend cloning your repo outside the S-Drive and use an SCP program like [WinSCP] to edit the files in Windows using whatever IDE you want if you want to code in Windows, but compile in Linux.

The only file you should ever modify to create your AI is the `ai.ts` file. All the other files are needed for the game to work. In addition, you should never be creating your own instances of the Game's classes, nor should you ever try to modify their variables. Instead, treat the Game and its members as a read only structure that represents the game state on the game server. You interact with it by calling the game object functions.

[Cadre]: https://github.com/siggame/Cadre
[JavaScript Client]: https://github.com/siggame/Joueur.js
[TypeScript]: http://www.typescriptlang.org/
[typescript]: https://www.npmjs.com/package/typescript
[TSLint]: https://www.npmjs.com/package/tslint
[Node.js]: https://nodejs.org/
[Node Version Manager]: https://github.com/creationix/nvm
[async/await]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function
[Visual Studio Code]: https://code.visualstudio.com/
[Vagrant]: https://www.vagrantup.com/
[Vagrant's guide]: https://www.vagrantup.com/docs/getting-started/
[Virtualbox]: https://www.virtualbox.org/wiki/Downloads
[Git Bash]: https://git-scm.com/downloads
[WinSCP]: https://winscp.net/
