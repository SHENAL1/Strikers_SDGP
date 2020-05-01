import { Component, OnInit } from '@angular/core';
import { FormControl, EmailValidator, Validators } from '@angular/forms';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Router } from '@angular/router';


@Component({
  selector: 'app-add-player',
  templateUrl: './add-player.component.html',
  styleUrls: ['./add-player.component.css']
})
export class AddPlayerComponent implements OnInit {

  //PhotoFormControl  = new FormControl();
  Short_nameFormControl  = new FormControl();
  Long_nameFormControl  = new FormControl();
  AgeFormControl  = new FormControl();
  HeightFormControl  = new FormControl();
  WeightFormControl  = new FormControl();
  NationalityFormControl  = new FormControl();
  ClubFormControl  = new FormControl();
  OverallFormControl  = new FormControl();
  PotentialFormControl  = new FormControl();
  ValueFormControl  = new FormControl();
  WageFormControl  = new FormControl();
  Preferred_FootFormControl  = new FormControl();
  International_ReputationFormControl  = new FormControl();
  Weak_FootFormControl  = new FormControl();
  Skill_MovesFormControl  = new FormControl();
  PositionFormControl  = new FormControl();
  Jersey_NumberFormControl  = new FormControl();
  Contract_Valid_UntilFormControl  = new FormControl();
  CrossingFormControl  = new FormControl();
  FinishingFormControl  = new FormControl();
  Heading_AccuracyFormControl  = new FormControl();
  Short_PassingFormControl  = new FormControl();
  VolleysFormControl  = new FormControl();
  DribblingFormControl  = new FormControl();
  CurveFormControl  = new FormControl();
  FK_AccuracyFormControl  = new FormControl();
  Long_PassingFormControl  = new FormControl();
  Ball_ControlFormControl  = new FormControl();
  AccelerationFormControl  = new FormControl();
  Sprint_SpeedFormControl  = new FormControl();
  AgilityFormControl  = new FormControl();
  ReactionsFormControl  = new FormControl();
  BalanceFormControl  = new FormControl();
  Shot_PowerFormControl  = new FormControl();
  JumpingFormControl  = new FormControl();
  StaminaFormControl  = new FormControl();
  StrengthFormControl  = new FormControl();
  Long_ShotsFormControl  = new FormControl();
  AggressionFormControl  = new FormControl();
  InterceptionsFormControl  = new FormControl();
  PositioningFormControl  = new FormControl();
  VisionFormControl  = new FormControl();
  PenaltiesFormControl  = new FormControl();
  ComposureFormControl  = new FormControl();
  MarkingFormControl  = new FormControl();
  Standing_TackleFormControl  = new FormControl();
  Sliding_TackleFormControl  = new FormControl();
  GK_DivingFormControl  = new FormControl();
  GK_HandlingFormControl  = new FormControl();
  GK_KickingFormControl  = new FormControl();
  GK_PositioningFormControl  = new FormControl();
  GKReflexesFormControl  = new FormControl();
  
  

  constructor(private http: HttpClient,public router:Router) { }

  ngOnInit() {
  }

  addNewPlayerDetails(){

    //var Photo= this.PhotoFormControl.value;
    var Short_name= this.Short_nameFormControl.value;
    var Long_name= this.Long_nameFormControl.value;
    var Age= this.AgeFormControl.value;
    var Height= this.HeightFormControl.value;
    var Weight= this.WeightFormControl.value;
    var Nationality= this.NationalityFormControl.value;
    var Club= this. ClubFormControl.value;
    var Overall= this.OverallFormControl.value;
    var Potential= this.PotentialFormControl.value;
    var Value= this.ValueFormControl.value;
    var Wage= this.WageFormControl.value;
    var Preferred_Foot= this.Preferred_FootFormControl.value;
    var International_Reputation= this.International_ReputationFormControl.value;
    var Weak_Foot= this.Weak_FootFormControl.value;
    var Skill_Moves= this.Skill_MovesFormControl.value;
    var Position= this.PositionFormControl.value;
    var Jersey_Number= this.Jersey_NumberFormControl.value;
    var Contract_Valid_Until= this.Contract_Valid_UntilFormControl.value;
    var Crossing= this.CrossingFormControl.value;
    var Finishing= this.FinishingFormControl.value;
    var Heading_Accuracy= this.Heading_AccuracyFormControl.value;
    var Short_Passing= this.Short_PassingFormControl.value;
    var Volleys= this.VolleysFormControl.value;
    var Dribbling= this.DribblingFormControl.value;
    var Curve= this.CurveFormControl.value;
    var FK_Accuracy= this.FK_AccuracyFormControl.value;
    var Long_Passing= this.Long_PassingFormControl.value;
    var Ball_Control= this.Ball_ControlFormControl.value;
    var Acceleration= this.AccelerationFormControl.value;
    var Sprint_Speed= this.Sprint_SpeedFormControl.value;
    var Agility= this.AgilityFormControl.value;
    var Reactions= this.ReactionsFormControl.value;
    var Balance= this.BalanceFormControl.value;
    var Shot_Power= this.Shot_PowerFormControl.value;
    var Jumping= this.JumpingFormControl.value;
    var Stamina= this.StaminaFormControl.value;
    var Strength= this.StrengthFormControl.value;
    var Long_Shots= this.Long_ShotsFormControl.value;
    var Aggression= this.AggressionFormControl.value;
    var Interceptions= this.InterceptionsFormControl.value;
    var Positioning= this.PositioningFormControl.value;
    var Vision= this.VisionFormControl.value;
    var Penalties= this.PenaltiesFormControl.value;
    var Composure= this.ComposureFormControl.value;
    var Marking= this.MarkingFormControl.value;
    var Standing_Tackle= this.Standing_TackleFormControl.value;
    var Sliding_Tackle= this.Sliding_TackleFormControl.value;
    var GK_Diving= this.GK_DivingFormControl.value;
    var GK_Handling= this.GK_HandlingFormControl.value;
    var GK_Kicking= this.GK_KickingFormControl.value;
    var GK_Positioning= this.GK_PositioningFormControl.value;
    var GKReflexes = this.GKReflexesFormControl.value;
  

  let body = new HttpParams({


    fromObject:{

        //'Photo':Photo,
        'Short_name':Short_name,
        'Long_name':Long_name,
        'Age':Age,
        'Height':Height,
        'Weight':Weight,
        'Nationality':Nationality,
        'Club':Club,
        'Overall':Overall,
        'Potential':Potential,
        'Value':Value,
        'Wage':Wage,
        'Preferred_Foot':Preferred_Foot,
        'International_Reputation':International_Reputation,
        'Weak_Foot':Weak_Foot,
        'Skill_Moves':Skill_Moves,
        'Position':Position,
        'Jersey_Number':Jersey_Number,
        'Contract_Valid_Until':Contract_Valid_Until,
        'Crossing':Crossing,
       'Finishing':Finishing,
        'Heading_Accuracy':Heading_Accuracy,
        'Short_Passing':Short_Passing,
        'Volleys':Volleys,
        'Dribbling':Dribbling,
        'Curve':Curve,
        'FK_Accuracy':FK_Accuracy,
        'Long_Passing':Long_Passing,
        'Ball_Control':Ball_Control,
        'Acceleration':Acceleration,
        'Sprint_Speed':Sprint_Speed,
        'Agility':Agility,
        'Reactions':Reactions,
        'Balance':Balance,
        'Shot_Power':Shot_Power,
        'Jumping':Jumping,
        'Stamina':Stamina,
        'Strength':Strength,
        'Long_Shots':Long_Shots,
        'Aggression':Aggression,
        'Interceptions':Interceptions,
        'Positioning':Positioning,
        'Vision':Vision,
        'Penalties':Penalties,
        'Composure':Composure,
        'Marking':Marking,
        'Standing_Tackle':Standing_Tackle,
        'Sliding_Tackle':Sliding_Tackle,
        'GK_Diving':GK_Diving,
        'GK_Handling':GK_Handling,
        'GK_Kicking':GK_Kicking,
        'GK_Positioning':GK_Positioning,
        'GKReflexes':GKReflexes
    
    }
  });

  var url = 'http://localhost:4000/players'

  this.http.post<any>(url,body).subscribe(
    data=>{
      
      alert("You have successfully added a player")
      this.router.navigate(['/login']);
    }
  )

  }

}

