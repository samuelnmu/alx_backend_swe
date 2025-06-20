const dotenv = require("dotenv");
dotenv.config();

const token = process.env.TOKEN;

module.exports = { token };
