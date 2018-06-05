import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  encounter = {
      location:"all",
      difficulty: 0,
      minMonsters: 1,
      maxMonsters: 15,
  }
  constructor(public navCtrl: NavController) {

  }
  logForm() {
    console.log(this.encounter)
  }
}
