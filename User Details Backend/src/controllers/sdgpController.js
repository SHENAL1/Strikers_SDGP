import mongoose from 'mongoose';
import { UserSchema} from '../models/sdgpModel';

const UserDetails = mongoose.model('UserDetails',UserSchema);

export const addNewUserDetails = (req,res) => {
    let newUserDetails = new UserDetails(req.body);

    newUserDetails.save((err, userDetails) => {
        if (err){
            res.send(err);
        }
        res.json(userDetails);
    });

}

export const getUserDetails = (req,res) => {
    UserDetails.find({}, (err, userDetails) => {
        if (err){
            res.send(err);
        }
        res.json(userDetails);
    });
}

export const getUserDetailsWithID = (req,res) => {
    UserDetails.findById(req.params.userID, (err, userDetails) => {
        if (err){
            res.send(err);
        }
        res.json(userDetails);
    });
}

export const updateUserDetails = (req,res) => {
    UserDetails.findOneAndUpdate({_id: req.params.userID}, req.body, { new: true, useFindAndModify:false}, (err, userDetails) => {
        if (err){
            res.send(err);
        }
        res.json(userDetails);
    });
}

export const deleteUserDetails = (req,res) => {
    UserDetails.remove({_id: req.params.userID}, (err, userDetails) => {
        if (err){
            res.send(err);
        }
        res.json({message: 'You are successfully deleted user deatils'});
    });
}


