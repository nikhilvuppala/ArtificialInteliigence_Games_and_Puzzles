// Please do not modify this file.
// Instead have a look at `README.md` for how to start writing you AI.

import { ArgumentParser } from "argparse";
import { run } from "./joueur/run";

process.title = "Joueur.ts Game Client";

const parser = new ArgumentParser({
    description: "Run the JavaScript client with options to connect to a game "
               + "server. Must provide a game name to play.",
});

parser.addArgument(["game"], {
    action: "store",
    help: "the name of the game you want to play on the server",
});

parser.addArgument(["-s", "--server"], {
    action: "store",
    defaultValue: "127.0.0.1",
    dest: "server",
    help: "the hostname or the server you want to connect to e.g. locahost:3000",
});

parser.addArgument(["-p", "--port"], {
    action: "store",
    defaultValue: 3000,
    dest: "port",
    help: "the port to connect to on the server. Can be defined on the server arg via server:port",
});

parser.addArgument(["-n", "--name"], {
    action: "store",
    dest: "playerName",
    help: "the name you want to use as your AI\"s player name",
});

parser.addArgument(["-i", "--index"], {
    action: "store",
    dest: "index",
    help: "the player number you want to be, with 0 being the first player",
});

parser.addArgument(["-w", "--password"], {
    action: "store",
    dest: "password",
    help: "the password required for authentication on official servers",
});

parser.addArgument(["-r", "--session"], {
    action: "store",
    defaultValue: "*",
    dest: "session",
    help: "the requested game session you want to play on the server",
});

parser.addArgument(["--gameSettings"], {
    action: "store",
    dest: "gameSettings",
    help: "Any settings for the game server to force. Must be url parms formatted (key=value&otherKey=otherValue)",
});

parser.addArgument(["--aiSettings"], {
    action: "store",
    dest: "aiSettings",
    help: "Any settings for the AI. Delimit pairs by an ampersand (key=value&otherKey=otherValue)",
});

parser.addArgument(["--printIO"], {
    action: "storeTrue",
    dest: "printIO",
    help: "(debugging) print IO through the TCP socket to the terminal",
});

run(parser.parseArgs()); // tslint:disable-line:no-unsafe-any
