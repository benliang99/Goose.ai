import { CredentialType, IDKitWidget } from "@worldcoin/idkit";
import type { ISuccessResult } from "@worldcoin/idkit";
import styles from "../styles/Home.module.css";

import { useState, useEffect } from "react";
import detectEthereumProvider from "@metamask/detect-provider";

export default function Home() {
  const [hasProvider, setHasProvider] = useState<boolean | null>(null);
  const initialState = { accounts: [] }; /* New */
  const [wallet, setWallet] = useState(initialState); /* New */

  useEffect(() => {
    const getProvider = async () => {
      const provider = await detectEthereumProvider({ silent: true });
      setHasProvider(Boolean(provider));
    };

    getProvider();
  }, []);

  const updateWallet = async (accounts: any) => {
    /* New */
    setWallet({ accounts }); /* New */
    setTimeout(() => {  setVerified(true); }, 2000);
  }; /* New */

  const handleConnect = async () => {
    /* New */
    let accounts = await window.ethereum.request({
      /* New */ method: "eth_requestAccounts" /* New */,
    }); /* New */
    updateWallet(accounts); /* New */
  };

  const [verified, setVerified] = useState(false);

  const onSuccess = (result: ISuccessResult) => {
    // This is where you should perform frontend actions once a user has been verified, such as redirecting to a new page
    setVerified(true);
  };

  const handleProof = async (result: ISuccessResult) => {
    const reqBody = {
      merkle_root: result.merkle_root,
      nullifier_hash: result.nullifier_hash,
      proof: result.proof,
      credential_type: result.credential_type,
      action: process.env.NEXT_PUBLIC_WLD_ACTION_NAME,
      signal: "",
    };
    fetch("/api/verify", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(reqBody),
    }).then(async (res: Response) => {
      if (res.status == 200) {
        console.log("Successfully verified credential.");
      } else {
        throw (
          new Error("Error: " + (await res.json()).code) ?? "Unknown error."
        );
      }
    });
  };

  const [isHovered, setIsHovered] = useState(false);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  const buttonStyle = {
    padding: "10px 20px",
    fontSize: "16px",
    fontWeight: "bold",
    borderRadius: "5px",
    color: "#fff",
    border: "none",
    cursor: "pointer",
    boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
    background: "linear-gradient(45deg, #ff0000, #00ff00, #0000ff, #ff0000)",
    backgroundSize: "200% 200%",
    animation: "gradientAnimation 5s ease infinite",
    transition: "background 0.3s",
  };

  return (
    <div className={styles.container}>
      {!verified && (
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            minHeight: "100vh",
          }}
        >
          <div>
            <h1
              style={{
                backgroundColor: "rgba(0, 0, 0, 0.5)",
                padding: "20px",
                fontSize: "36px",
                color: "#fff",
                textAlign: "center",
              }}
            >
              Mint your very own ETHWaterloo POAP using Goose.ai!
            </h1>
            <h2
              style={{
                backgroundColor: "rgba(0, 0, 0, 0.5)",
                padding: "20px",
                fontSize: "24px",
                color: "#fff",
                textAlign: "center",
              }}
            >
              Meet Goose.ai, the cyber companion that will steal your heart with
              every honk. This delightful goose is here to revolutionize your
              digital journey with cuddles and unwavering loyalty. He's not your
              average sidekick – he's a feathered friend that will keep you safe
              and snug in the ever-changing cyber realm.
            </h2>
          </div>
          <h1>&nbsp;</h1>

          <div>Injected Provider {hasProvider ? 'DOES' : 'DOES NOT'} Exist</div>
          <h1>&nbsp;</h1>
          <button
            onClick={handleConnect}
            style={{
              padding: "10px 20px",
              fontSize: "16px",
              fontWeight: "bold",
              borderRadius: "5px",
              color: "#fff",
              backgroundColor: "orange",
              border: "none",
              cursor: "pointer",
              boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
              transition: "background-color 0.3s",
            }}
          >
            Connect MetaMask
          </button>

          <h1>&nbsp;</h1>
          <p className="text-13 text-c2a4e5">Powered by MetaMask SDK</p>

          <h1>&nbsp;</h1>

          {wallet.accounts.length > 0 /* New */ && (
            <h1>Wallet Accounts: {wallet.accounts[0]}</h1>
          )}
          <IDKitWidget
            action={process.env.NEXT_PUBLIC_WLD_ACTION_NAME!}
            onSuccess={onSuccess}
            handleVerify={handleProof}
            app_id={process.env.NEXT_PUBLIC_WLD_APP_ID!}
            credential_types={[CredentialType.Orb, CredentialType.Phone]}
          >
            {({ open }) => (
              <button
                onClick={open}
                style={{
                  padding: "10px 20px",
                  fontSize: "16px",
                  fontWeight: "bold",
                  borderRadius: "5px",
                  color: "#fff",
                  backgroundColor: "black",
                  border: "none",
                  cursor: "pointer",
                  boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
                  transition: "background-color 0.3s",
                }}
              >
                Verify with World ID
              </button>
            )}
          </IDKitWidget>
          <h1>&nbsp;</h1>
          <p className="text-13 text-c2a4e5">Powered by WorldCoin</p>
        </div>
      )}
      {verified && (
        <iframe
          src="https://creator.voiceflow.com/prototype/64964832cba8be000738c63e"
          width="100%"
          height="100%"
        ></iframe>
        
      )}
      { wallet.accounts.length > 0 &&                /* New */
        <div>Wallet Accounts: { wallet.accounts[0] }</div>
      }
    </div>
  );
}
