const mongoose = require('mongoose');
/** 
 * @fileOverview Define the user model to database
 * */

const userSchema = mongoose.Schema({
    _id:mongoose.Schema.Types.ObjectId,
    firstName: {
        type: String,
        required: 'Please enter the first name'

    },
    lastName: {
        type: String,
        required: 'Please enter the first name'
    },
    userName: {
        type: String,
        required: 'Please enter the user name',
        unique: true,
    },
    email: {
        type: String,
        match:/[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/
    },
    password: {
        type: String
    },
    created_Date: {
        type: Date,
        default:Date.now
    }
});

module.exports = mongoose.model('UserDetails',userSchema);