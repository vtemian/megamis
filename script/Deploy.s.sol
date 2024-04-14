// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Script.sol"; // solhint-disable-line
import {Upgrades} from "openzeppelin-foundry-upgrades/Upgrades.sol";

import {Megamis} from "../src/Megamis.sol";

contract DeployV1 is Script {
    function setUp() public {}

    function run() public {
        uint256 privateKey = vm.envUint("PRIVATE_KEY");
        address deployer = vm.envAddress("DEPLOYER");

        vm.startBroadcast(privateKey);

        address proxy = Upgrades.deployTransparentProxy(
            "../src/Megamis.sol",
            deployer,
            abi.encodeCall(Megamis.initialize, (deployer))
        );

        vm.stopBroadcast();
    }
}