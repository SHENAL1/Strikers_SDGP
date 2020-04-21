const mongoose = require('mongoose');

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
        required: 'Please enter the user name'
    },
    email: {
        type: String
    },
    password: {
        type: String
    },
    created_Date: {
        type: Date,
        default:Date.now
    }
});

module.exports = mongoose.model('User',userSchema);