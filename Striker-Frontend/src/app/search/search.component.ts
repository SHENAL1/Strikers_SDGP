import { Component } from '@angular/core';
import { PlayersService } from '../players.service';


@Component({
  selector: 'my-app',
  templateUrl: './search.component.html',
  styleUrls: [ './search.component.css' ]
})
export class SearchComponent  {
  title = 'Search Your Players';
  Store:any[];
  searchText;
  
  constructor(public playersService:PlayersService) { 
    this.playersService.getyo().subscribe(Update=>{this.Store=Update});
  }
}
