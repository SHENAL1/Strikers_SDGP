import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class RatingsService {

  constructor(private http:HttpClient) { }

  goalkeeper(){
    return this.http.get<any[]>('http://127.0.0.1:5000/goalkeeper');
  
  }

  leftWingBack(){
    return this.http.get<any[]>('http://127.0.0.1:5000/leftWingBack');
  
  }

  centreMidfielder(){
    return this.http.get<any[]>('http://127.0.0.1:5000/centreMidfielder');
  
  }

  rightWingBack(){
    return this.http.get<any[]>('http://127.0.0.1:5000/rightWingBack');
  
  }
  rightWingAttacker(){
    return this.http.get<any[]>('http://127.0.0.1:5000/rightWingAttacker');
  
  }
  leftWingAttacker(){
    return this.http.get<any[]>('http://127.0.0.1:5000/leftWingAttacker');
  
  }
  rightCentreMidfielder(){
    return this.http.get<any[]>('http://127.0.0.1:5000/rightCentreMidfielder');
  
  }
  leftCentreMidfielder(){
    return this.http.get<any[]>('http://127.0.0.1:5000/leftCentreMidfielder');
  
  }
  striker(){
    return this.http.get<any[]>('http://127.0.0.1:5000/striker');
  
  }
  leftCenterDefender(){
    return this.http.get<any[]>('http://127.0.0.1:5000/leftCenterDefender');
  
  }
  rightCenterDefender(){
    return this.http.get<any[]>('http://127.0.0.1:5000/rightCenterDefender');
  
  }
}
