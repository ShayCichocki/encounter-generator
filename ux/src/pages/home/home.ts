import { Component } from '@angular/core';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
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
