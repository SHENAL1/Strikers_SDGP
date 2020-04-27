import{Injectable}from '@angular/core';
import { CanActivate,Router,RouterStateSnapshot,ActivatedRouteSnapshot } from "@angular/router";

@Injectable({
    providedIn:'root'
})
export class SessionService{

    constructor(
        private router:Router
    ){}

    private auth:boolean = false;
    private id : string ='0';
    private name: string = 'Guest'

public setAuth(auth:boolean){
    this.auth =auth;
    localStorage.setItem('auth',''+auth);
}
getAuth():boolean{
    return localStorage.getItem('auth')=='true';
}

public setID(id:string){
    this.id =id;
    console.log("ID="+id);
    localStorage.setItem('id',id);
}

getID():string{
    return localStorage.getItem('id')

}
public setName(name:string){
    this.name = name;
    localStorage.setItem('name',name);
}

getName():string{
    return localStorage.getItem('name')
}

canActivate(route:ActivatedRouteSnapshot,state:RouterStateSnapshot):boolean{
    if(this.getAuth()){
        return true;

    }else{
        this.router.navigate(['/login']);
        return false;
    }
}

}