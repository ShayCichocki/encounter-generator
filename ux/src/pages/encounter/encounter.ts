import { Component } from '@angular/core';
import { monsterService } from '../../providers/monsterService';

@Component({
  selector: 'page-encounter',
  templateUrl: 'encounter.html',
})
export class EncounterPage {
  monsters: string[];
  CR: number;

  constructor(private monsterService: monsterService){}
  
  ionViewDidEnter(){
    this.monsters = this.monsterService.getMonsterList();
    this.CR = this.monsterService.totalCR();
  }

  addHero(){
    
  }

}
