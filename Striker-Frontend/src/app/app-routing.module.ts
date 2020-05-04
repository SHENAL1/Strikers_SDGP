import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SignupComponent } from './signup/signup.component';
import { LoginComponent } from './login/login.component';
import { AddPlayerComponent } from './add-player/add-player.component';
import { MenuComponent } from './menu/menu.component';
import { HomeComponent } from './home/home.component';
import { RatingsComponent } from './ratings/ratings.component';
import { AverageComponent } from './average/average.component';
import { AboutUsComponent } from './about-us/about-us.component';
import { FineComponent } from './fine/fine.component';
import { SearchComponent } from './search/search.component';
import { ViewPlayersComponent } from './view-players/view-players.component';

import { HttpClientModule } from '@angular/common/http';



const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  {path:'signup',component:SignupComponent},
  {path:'login',component:LoginComponent},
  {path:'add-player',component:AddPlayerComponent},
  {path:'menu',component:MenuComponent},
  {path:'home',component:HomeComponent},
  {path:'ratings',component:RatingsComponent},
  {path:'average',component:AverageComponent},
  {path:'about-us',component:AboutUsComponent},
  {path:'fine',component:FineComponent},
  {path:'search',component:SearchComponent},
  {path:'view-players',component:ViewPlayersComponent}
  
 ];

@NgModule({
  imports: [RouterModule.forRoot(routes),HttpClientModule, ],
  
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [SignupComponent,LoginComponent,AddPlayerComponent,MenuComponent,HomeComponent,RatingsComponent,AverageComponent,AboutUsComponent,FineComponent,SearchComponent,ViewPlayersComponent]