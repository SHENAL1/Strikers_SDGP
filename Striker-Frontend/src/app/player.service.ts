import { Injectable } from '@angular/core';
import{HttpClient,HttpHeaders} from '@angular/common/http';
import{Player} from '../player';

@Injectable({
  providedIn: 'root'
})
export class PlayerService {
private baseUri:string="http://localhost:4000";
private headers = new HttpHeaders().set('Content-Type' , 'application/json');

  constructor(private http:HttpClient) { 
  
  }
  getPlayer(){
        return this.http.get(this.baseUri+'/players',{headers:this.headers});
  }
  updatePlayer(player:Player){
    return this.http.put(this.baseUri+'/:playerId',player,{headers:this.headers})
  }
  deletePlayer(id:string){
    return this.http.delete(this.baseUri+'/:playerId'+id,{headers:this.headers})
  }
}
