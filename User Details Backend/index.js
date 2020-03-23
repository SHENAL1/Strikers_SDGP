import express from 'express';
import routes from './src/routes/sdgpRoutes';
import mongoose from 'mongoose';
import bodyParser from 'body-parser';


const app = express();
const PORT = 4000;

//mongoose connection

mongoose.Promise = global.Promise;
mongoose.connect('mongodb+srv://admin:admin@striker-spfii.mongodb.net',{
    useNewUrlParser: true,
    useUnifiedTopology: true
});

//bodyparser Connection
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

routes(app);

app.get('/', (req, res) =>
    res.send(`Node and express server running on port ${PORT}`)
);

app.listen(PORT, () =>
    console.log(`Your server is running on port ${PORT}`)
);