import { Component, OnInit } from '@angular/core';
import { PlayersService } from '../players.service';

@Component({
  selector: 'app-fine',
  templateUrl: './fine.component.html',
  styleUrls: ['./fine.component.css']
})
export class FineComponent  {
  title = 'Angular Search Using ng2-search-filter';
  searchText;
  
  Store:any[];
  constructor(public playersService:PlayersService) { 
    this.playersService.getyo().subscribe(Update=>{this.Store=Update});
  }

 

}
