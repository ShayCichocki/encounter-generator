import { Component } from '@angular/core';
import { NavController, ModalController } from 'ionic-angular';
import { DataFinder } from '../../providers/datafinder';
import { CreaturePage } from '../creature/creature';
import { monsterService } from '../../providers/monsterService';

@Component({
  selector: 'page-creature-search',
  templateUrl: 'creature-search.html',
})
export class CreatureSearchPage{
  monsterList: any;

  constructor(private dataFinder: DataFinder, public navCtrl: NavController, private modalCtrl: ModalController, private monsterService: monsterService){}

  ionViewDidLoad() {
    this.dataFinder.getJSONDataAsync("../assets/data/simplified-monsters.json").then(data => {
      console.log(data);
      this.SetQueryOptionsData(data);
    });
  }

  SetQueryOptionsData(data : any) {
    this.monsterList = data
  }

  onViewMonster(monster){
    const modal = this.modalCtrl.create(CreaturePage, monster);
    modal.present();
    modal.onDidDismiss((add: boolean) => {
      if(add){
        this.monsterService.addMonsterToList(monster);
      }
      console.log(add);
    })
  }
}
