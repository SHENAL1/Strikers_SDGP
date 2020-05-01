import { Component, OnInit } from '@angular/core';
import { RatingsService } from '../ratings.service';


@Component({
  selector: 'app-ratings',
  templateUrl: './ratings.component.html',
  styleUrls: ['./ratings.component.css']
})
export class RatingsComponent implements OnInit {

  goalkeeperStore:any[];
  leftWingBackStore:any[];
  centreMidfielderStore:any[];
  rightWingBackStore:any[];
  rightWingAttackerStore:any[];
  leftWingAttackerStore:any[];
  rightCentreMidfielderStore:any[];
  leftCentreMidfielderStore:any[];
  strikerStore:any[];
  leftCenterDefenderStore:any[];
  rightCenterDefenderStore:any[];

  show: boolean = false;
  show1: boolean = false;
  show2: boolean = false;
  show3: boolean = false;
  show4: boolean = false;
  show5: boolean = false;
  show6: boolean = false;
  show7: boolean = false;
  show8: boolean = false;
  show9: boolean = false;
  show10: boolean = false;

  constructor(public ratingsServices:RatingsService) { 

    this.ratingsServices.goalkeeper().subscribe(goalkeeperlist=>{this.goalkeeperStore=goalkeeperlist});
    this.ratingsServices.leftWingBack().subscribe(leftWingBacklist=>{this.leftWingBackStore=leftWingBacklist});
    this.ratingsServices.centreMidfielder().subscribe(centreMidfielderlist=>{this.centreMidfielderStore=centreMidfielderlist});
    this.ratingsServices.rightWingBack().subscribe(rightWingBacklist=>{this.rightWingBackStore=rightWingBacklist});
    this.ratingsServices.rightWingAttacker().subscribe(rightWingAttackerlist=>{this.rightWingAttackerStore=rightWingAttackerlist});
    this.ratingsServices.leftWingAttacker().subscribe(leftWingAttackerlist=>{this.leftWingAttackerStore=leftWingAttackerlist});
    this.ratingsServices.rightCentreMidfielder().subscribe(rightCentreMidfielderlist=>{this.rightCentreMidfielderStore=rightCentreMidfielderlist});
    this.ratingsServices.leftCentreMidfielder().subscribe(leftCentreMidfielderlist=>{this.leftCentreMidfielderStore=leftCentreMidfielderlist});
    this.ratingsServices.striker().subscribe(strikerlist=>{this.strikerStore=strikerlist});
    this.ratingsServices.leftCenterDefender().subscribe(leftCenterDefenderlist=>{this.leftCenterDefenderStore=leftCenterDefenderlist});
    this.ratingsServices.rightCenterDefender().subscribe(rightCenterDefenderlist=>{this.rightCenterDefenderStore=rightCenterDefenderlist});
  }

  ngOnInit() {
  }


}
