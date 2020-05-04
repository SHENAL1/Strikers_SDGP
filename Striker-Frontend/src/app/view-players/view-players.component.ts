import { Component, OnInit } from '@angular/core';
import { PlayersService } from '../players.service';
import { FormControl, EmailValidator, Validators } from '@angular/forms';
import { HttpClient, HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-view-players',
  templateUrl: './view-players.component.html',
  styleUrls: ['./view-players.component.css']
})
export class ViewPlayersComponent {

  Store:any[];
  currentTutorial = null;

  constructor(public playersService:PlayersService) { 
    this.playersService.getyo().subscribe(Update=>{this.Store=Update});
  }

}
