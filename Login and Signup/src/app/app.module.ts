import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormControl} from '@angular/forms';
import {FormGroup} from '@angular/forms';
import {Validators} from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';




import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SignupComponent } from './signup/signup.component';
import { LoginComponent } from './login/login.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AddPlayerComponent } from './add-player/add-player.component';
import { MenuComponent } from './menu/menu.component';
import { UpdatePlayerComponent } from './update-player/update-player.component';
import { DeletePlayerComponent } from './delete-player/delete-player.component';
import { AverageComponent } from './average/average.component';
import { HomeComponent } from './home/home.component';
import { RatingsComponent } from './ratings/ratings.component';

@NgModule({
  declarations: [
    AppComponent,
    SignupComponent,
    LoginComponent,
    AddPlayerComponent,
    MenuComponent,
    UpdatePlayerComponent,
    DeletePlayerComponent,
    AverageComponent,
    HomeComponent,
    RatingsComponent,
    
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    FormsModule,
    
    

    
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
