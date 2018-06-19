import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { CreatureSearchPage } from './creature-search';

@NgModule({
  declarations: [
    CreatureSearchPage,
  ],
  imports: [
    IonicPageModule.forChild(CreatureSearchPage),
  ],
})
export class CreatureSearchPageModule {}
