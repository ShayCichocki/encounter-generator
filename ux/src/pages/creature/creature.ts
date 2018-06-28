import { Component } from '@angular/core';
import { ViewController, NavParams } from 'ionic-angular';

@Component({
  selector: 'page-creature',
  templateUrl: 'creature.html',
})
export class CreaturePage {
  name: string;
  CR: number;
  XP: number;
  environment: string;
  mobs = [];


  constructor(private viewCtrl: ViewController, private navParams: NavParams){}

  ionViewDidLoad(){
    this.name = this.navParams.get('name')
    this.CR = this.navParams.get('cr')
    this.XP = this.navParams.get('xp')
    this.environment = this.navParams.get('environment')
  }

  addCreature(){
    this.mobs.push(this.name);
    console.log(this.mobs)
  }

  onClose(add = false){
    this.viewCtrl.dismiss(add);
  }

}
