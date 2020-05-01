import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SignupComponent } from './signup/signup.component';
import { LoginComponent } from './login/login.component';
import { AddPlayerComponent } from './add-player/add-player.component';
import { MenuComponent } from './menu/menu.component';
import { HomeComponent } from './home/home.component';
import { RatingsComponent } from './ratings/ratings.component';

import { HttpClientModule } from '@angular/common/http';



const routes: Routes = [
  {path:'signup',component:SignupComponent},
  {path:'login',component:LoginComponent},
  {path:'add-player',component:AddPlayerComponent},
  {path:'menu',component:MenuComponent},
  {path:'home',component:HomeComponent},
  {path:'ratings',component:RatingsComponent}
  
 ];

@NgModule({
  imports: [RouterModule.forRoot(routes),HttpClientModule, ],
  
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [SignupComponent,LoginComponent,AddPlayerComponent,MenuComponent,HomeComponent,RatingsComponent]