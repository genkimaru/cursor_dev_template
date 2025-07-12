#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

function copyRecursive(src, dest) {
  if (!fs.existsSync(dest)) {
    fs.mkdirSync(dest, { recursive: true });
  }
  for (const file of fs.readdirSync(src)) {
    const srcFile = path.join(src, file);
    const destFile = path.join(dest, file);
    const stat = fs.statSync(srcFile);
    if (stat.isDirectory()) {
      copyRecursive(srcFile, destFile);
    } else {
      fs.copyFileSync(srcFile, destFile);
    }
  }
}

(function () {
  const targetDir = process.argv[2] || ".";

  const templateDir = path.join(__dirname, "template");
  copyRecursive(templateDir, targetDir);

  console.log("✅ Project created successfully!");
})();
