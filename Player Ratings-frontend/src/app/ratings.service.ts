import { Injectable } from '@angular/core';
import{HttpClient,HttpParams }from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class RatingsService {

  constructor(private http:HttpClient) {

   }
   getratings1(){
     
     return this.http.get<any[]>('http://127.0.0.1:5000/goalkeeper');
     
   }

   getratings2(){
     
    return this.http.get<any[]>('http://127.0.0.1:5000/leftWingBack');
    
  }
  getratings3(){
     
    return this.http.get<any[]>('http://127.0.0.1:5000/centreMidfielder');
    
  }
  getratings4(){
     
    return this.http.get<any[]>('http://127.0.0.1:5000/rightWingBack');
    
  }
  getratings5(){
     
    return this.http.get<any[]>('http://127.0.0.1:5000/rightWingAttacker');
    
  }
  getratings6(){
     
    return this.http.get<any[]>('http://127.0.0.1:5000/leftWingAttacker');
    
  }
  getratings7(){
     
    return this.http.get<any[]>('http://127.0.0.1:5000/rightCentreMidfielder');
    
  }
  getratings8(){
     
    return this.http.get<any[]>('http://127.0.0.1:5000/leftCentreMidfielder');
    
  }
  getratings9(){
     
    return this.http.get<any[]>('http://127.0.0.1:5000/striker');
    
  }
  getratings10(){
     
    return this.http.get<any[]>('http://127.0.0.1:5000/leftCenterDefender');
    
  }
  getratings11(){
     
    return this.http.get<any[]>('http://127.0.0.1:5000/rightCenterDefender');
    
  }
   
}
