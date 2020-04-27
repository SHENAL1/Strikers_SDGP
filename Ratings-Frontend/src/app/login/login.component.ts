import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { HttpClient, HttpParams } from '@angular/common/http';
import { SessionService } from '../session';
import { Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  passwordFormControl = new FormControl();
  userNameFormControl = new FormControl('',[
    Validators.required,
    
  ]

  );

  constructor(private http:HttpClient,private session: SessionService,public router:Router) { }

  ngOnInit(){
  }

  login() {

    var userName = this.userNameFormControl.value;
    var password = this.passwordFormControl.value;

    let body= new HttpParams({
      fromObject:{
        'userName':userName,
        'password':password
      }

    });

    var url="http://localhost:4000/user/login";
    console.log(body)

    this.http.post<any>(url,body).subscribe(
      data =>{
        if(data['auth']){
          this.session.setAuth(true);
          this.session.setID(data['_id']);
          this.session.setName(data['name']);

          this.router.navigate(
            ['/menu']
          );
          alert("Login success")
        }else{
          alert("Invalid UserName or Password")
        }
      }
    )
  }

}

