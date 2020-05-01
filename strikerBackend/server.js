/**
 * 
 *  @fileoverview RESTful Api for striker: Football player recommendation system
 *  @author Kavindu Jayawardhana and Shenal Anthony
 * 
 */

const http = require('http');
const app = require('./app')

const port = process.env.PORT || 4200;

const server = http.createServer(app);

server.listen(port, console.log(`Server started on port ${port}`));