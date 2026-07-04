const { spawn } = require("child_process");
const path = require("path");

const serverPaths = {
  darwin: "/Users/christopherzornes/Documents/Codex/mcp-servers/rpgmaker-mz-mcp/dist/index.js",
  win32: "C:\\Users\\elzor\\OneDrive\\Documents\\RMMZ\\tools\\rpgmaker-mz-mcp\\dist\\index.js",
};

const serverPath = process.env.RPGMAKER_MZ_MCP_SERVER || serverPaths[process.platform];
const projectPath = process.env.RPGMAKER_PROJECT_PATH ||
  "/Users/christopherzornes/Documents/GitHub/TheLastSwordProtocol-Game";

if (!serverPath) {
  console.error(`Unsupported platform for RPG Maker MZ MCP: ${process.platform}`);
  process.exit(1);
}

const child = spawn("node", [serverPath], {
  stdio: "inherit",
  env: {
    ...process.env,
    RPGMAKER_PROJECT_PATH: projectPath,
  },
});

child.on("exit", code => process.exit(code ?? 0));
