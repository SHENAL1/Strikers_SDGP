import { Component, OnInit } from '@angular/core';
import { RatingsService } from '../ratings.service';
import{HttpClient,HttpParams }from '@angular/common/http';
import { Router} from '@angular/router';

@Component({
  selector: 'app-ratings',
  templateUrl: './ratings.component.html',
  styleUrls: ['./ratings.component.css']
})
export class RatingsComponent implements OnInit {
  show: boolean = false;

  ratingsStore1:any[];
  ratingsStore2:any[];
  ratingsStore3:any[];
  ratingsStore4:any[];
  ratingsStore5:any[];
  ratingsStore6:any[];
  ratingsStore7:any[];
  ratingsStore8:any[];
  ratingsStore9:any[];
  ratingsStore10:any[];
  ratingsStore11:any[];


  constructor(public RatingsService:RatingsService) { 
    this.RatingsService.getratings1().subscribe(ratingslist1=>{this.ratingsStore1=ratingslist1});
    this.RatingsService.getratings2().subscribe(ratingslist2=>{this.ratingsStore1=ratingslist2});
    this.RatingsService.getratings3().subscribe(ratingslist3=>{this.ratingsStore1=ratingslist3});
    this.RatingsService.getratings4().subscribe(ratingslist4=>{this.ratingsStore1=ratingslist4});
    this.RatingsService.getratings5().subscribe(ratingslist5=>{this.ratingsStore1=ratingslist5});
    this.RatingsService.getratings6().subscribe(ratingslist6=>{this.ratingsStore1=ratingslist6});
    this.RatingsService.getratings7().subscribe(ratingslist7=>{this.ratingsStore1=ratingslist7});
    this.RatingsService.getratings8().subscribe(ratingslist8=>{this.ratingsStore1=ratingslist8});
    this.RatingsService.getratings9().subscribe(ratingslist9=>{this.ratingsStore1=ratingslist9});
    this.RatingsService.getratings10().subscribe(ratingslist10=>{this.ratingsStore1=ratingslist10});
    this.RatingsService.getratings11().subscribe(ratingslist11=>{this.ratingsStore1=ratingslist11});
    
  }

  ngOnInit() {
  }


}
