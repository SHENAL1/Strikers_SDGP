import mongoose from 'mongoose';

const Schema = mongoose.Schema;


export const UserSchema = new Schema({
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
    confirmPasssword: {
        type: String
    },
    created_Date: {
        type: Date,
        default:Date.now
    }
});
