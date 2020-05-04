import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';

const baseUrl = 'http://localhost:4000/players/:playersId';
const Url="http://localhost:4000/players"

@Injectable({
  providedIn: 'root'
})
export class PlayersService {

  constructor(private http:HttpClient) { }

  getyo(){
    return this.http.get<any[]>('http://localhost:4000/players');
  //   Observable<DataInRisk[]>{
  // ;
  }

  get(_id) {
    return this.http.get(`${Url}/${_id}`);
  }


  delete(_id) {
    return this.http.delete(`${baseUrl}/${_id}`);
  }


}
