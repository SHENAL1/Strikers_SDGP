import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { EmailValidator } from '@angular/forms';
import { Validators } from '@angular/forms';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Router } from '@angular/router';
import {FormGroup} from '@angular/forms';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  userNameFormControl  = new FormControl('');
  firstNameFormControl  = new FormControl('');
  lastNameFormControl  = new FormControl('');
  passwordFormControl  = new FormControl('');
  
  emailFormControl  = new FormControl('',[
    Validators.required,
    Validators.email,
  ]);

  constructor(private http: HttpClient,public router:Router) { }

  ngOnInit(): void {
  }

  

  register(){
    var userName = this.userNameFormControl.value;
    var firstName = this.firstNameFormControl.value;
    var lastName = this.lastNameFormControl.value;
    var email = this.emailFormControl.value;
    var password = this.passwordFormControl.value;
    
  

  let body = new HttpParams({


    fromObject:{
      'userName':userName,
      'firstName':firstName,
      'lastName':lastName, 
      'email':email,
      'password':password
    }
  });

  var url = 'http://localhost:4000/user/signup'
  
  this.http.post<any>(url,body).subscribe(
    data=>{
      
      alert("You have successfully registered")
      this.router.navigate(['/login']);
    }
  )

  }
}


