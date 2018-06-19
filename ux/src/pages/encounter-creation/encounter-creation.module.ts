import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { EncounterCreationPage } from './encounter-creation';

@NgModule({
  declarations: [
    EncounterCreationPage,
  ],
  imports: [
    IonicPageModule.forChild(EncounterCreationPage),
  ],
})
export class EncounterCreationPageModule {}
