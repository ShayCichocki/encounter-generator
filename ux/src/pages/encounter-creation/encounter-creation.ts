import { Component } from '@angular/core';


@Component({
  selector: 'page-encounter-creation',
  templateUrl: 'encounter-creation.html',
})

export class EncounterCreationPage {
  encounter = {
      location:"all",
      difficulty: 0,
      minMonsters: 1,
      maxMonsters: 15
  }
  logForm() {
    console.log(this.encounter)
  }
}
