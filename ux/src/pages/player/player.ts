import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';

@Component({
  selector: 'player',
  templateUrl: 'player.html'
})
export class PlayerPage {
  player = {
      level: 1
  }
  constructor(public navCtrl: NavController) {

  }
  logForm() {
    console.log(this.player)
  }
}
