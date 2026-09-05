# Mortal Shell II: Feature Scope

Status: Module concept - not implemented. Checked 2026-09-05.

The items below are proposed capabilities. They are not release notes or a list of working features.

## Shell development

Investigate local progression editing with a readable summary of the affected Shell and values.

Acceptance: identify the supported game build and affected state; demonstrate the intended result; test transitions and persistence; document the original value or baseline and any restoration limits.

## Respec planning

Plan resource comparisons around the documented Mether's Severance system, keeping in-game mechanics separate from proposed app actions.

Acceptance: identify the supported game build and affected state; demonstrate the intended result; test transitions and persistence; document the original value or baseline and any restoration limits.

## Tarstone budgets

Explore bounded Glimpse and Tarcore adjustments after validating item identifiers and resource storage.

Acceptance: identify the supported game build and affected state; demonstrate the intended result; test transitions and persistence; document the original value or baseline and any restoration limits.

## Boss practice

Design encounter profiles with adjustable damage assistance and a preserved baseline.

Acceptance: identify the supported game build and affected state; demonstrate the intended result; test transitions and persistence; document the original value or baseline and any restoration limits.

## Combat pacing

Research practice-speed adjustments and their effect on timing, animation and scripted encounters.

Acceptance: identify the supported game build and affected state; demonstrate the intended result; test transitions and persistence; document the original value or baseline and any restoration limits.

## Patch profiles

Store the game build beside each planned configuration so outdated balance data can be identified.

Acceptance: identify the supported game build and affected state; demonstrate the intended result; test transitions and persistence; document the original value or baseline and any restoration limits.

## Shared application architecture

This theme is one adapter for a common application. The shared interface can manage profiles and show change previews; each game adapter must implement and validate its own behaviour. No universal memory addresses, item identifiers, save paths or hotkeys are supplied.

## Session scope

The proposed game-state assistance is scoped to the single-player game. Profile restoration must account for the complete relevant state, including any separate world and character data.

## First implementation target

A player wants to compare two Shell builds before investing resources. The proposed toolkit would show both plans, calculate their documented costs and record a separate practice profile for each.
