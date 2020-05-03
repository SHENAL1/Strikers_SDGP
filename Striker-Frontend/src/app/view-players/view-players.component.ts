import { Component, OnInit } from '@angular/core';
import {PlayerService} from '../player.service';
import {Player} from '../player'


@Component({
  selector: 'app-view-players',
  templateUrl: './view-players.component.html',
  styleUrls: ['./view-players.component.css']
})
export class ViewPlayersComponent implements OnInit {

  private players:Player[];
  constructor(private playerService:PlayerService) { }

  ngOnInit(): void {
    this.getPlayer();
  }
  getPlayer(){
    this.playerService.getPlayer().subscribe(
      data=>{
        console.log(data);
      },
      error=>{
        console.log(error)
      }
    )
  }
}

  
