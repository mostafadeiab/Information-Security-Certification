const express = require('express');
const app = express();
const helmet = require('helmet')
app.use(helmet())
app.use(helmet.hidePoweredBy({ setTo: 'PHP 4.2.0' }))
app.use(helmet.frameguard({action: 'deny'}))
app.use(helmet.xssFilter())
app.use(helmet.noSniff())
app.use(helmet.ieNoOpen())

var ninetyDaysInSeconds = 90*24*60*60;

app.use(helmet.hsts({maxAge: ninetyDaysInSeconds, force: true}))
app.use(helmet.dnsPrefetchControl())
app.use(helmet.noCache())
app.use(helmet.contentSecurityPolicy({directives:{defaultSrc: ["'self'"], scriptSrc: ["'self'", "trusted-cdn.com"]}}))

module.exports = app;
const api = require('./server.js');
app.use(express.static('public'));
app.disable('strict-transport-security');
app.use('/_api', api);
app.get("/", function (request, response) {
  response.sendFile(__dirname + '/views/index.html');
});
let port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Your app is listening on port ${port}`);
});
