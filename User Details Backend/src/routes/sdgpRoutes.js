import { addNewUserDetails,
        getUserDetails,
        getUserDetailsWithID,
        updateUserDetails,
        deleteUserDetails

} from '../controllers/sdgpController';

const routes = (app) => {
    app.route('/userDetails')
        .get((req, res, next) => {
            //middleware
            console.log(`Request from: ${req.originalUrl}`)
            console.log(`Request type: ${req.method}`)
            next();
        },getUserDetails)
        
        //Post Endpoint
        .post(addNewUserDetails)

    app.route('/userDetails/:userID')
        //get a specific user Details
        .get(getUserDetailsWithID)

        //updating a selected user
        .put(updateUserDetails)

        //deleting a selected user
        .delete(deleteUserDetails);
    }

export default routes;